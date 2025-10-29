#!/usr/bin/env bash

function echo2(){
    echo >&2 "$@"
}

if [[ "$1" == "-h" ]]; then
    echo "Usage: crypt-to-root.sh [\$FILE-TO-ENCRYPT [output file]]"
    echo "e.g.: crypt-to-root.sh foo.txt"
    echo "use crypt-to-root.sh without any arguments to encrypt from stdin instead"
    echo "use 'crypt-to-root.sh - -' to encrypt from stdin to stdout"
    exit 0
fi

cmd_exists()
{
    command -v "$1" >/dev/null 2>&1
}

need_tool()
{
    if ! cmd_exists $1 ; then
        echo2 "This tool needs the $1 executable in order to work. Please install it!"
        exit 1
    fi
}

# Ensure we have required tools
need_tool gpg
need_tool awk
need_tool mktemp
need_tool wget
need_tool basename

KEYSURL="https://infra.apache.org/tools/infrastructure-root.asc"

INPUTFILE=$1
TMPDIR=`mktemp -d`

# If no filename is specified, read from stdin instead
if [[ -z "$INPUTFILE" ]]; then
    INPUTFILE='-'
    OUTPUTFILE=${TMPDIR}/message.asc
else
    if [[ -n $2 ]]; then
        OUTPUTFILE=$2
    else
        BASENAME=`basename $INPUTFILE` # allow for files in other directories
        OUTPUTFILE=${TMPDIR}/${BASENAME}.asc
    fi
fi


echo2 "Importing ${KEYSURL} into ${TMPDIR}/keyring.gpg"
wget -q -O - ${KEYSURL} | gpg --no-default-keyring --quiet --keyring ${TMPDIR}/keyring.gpg --import -

echo2 "Removing any expired or revoked keys"
gpg --no-default-keyring --quiet --keyring ${TMPDIR}/keyring.gpg --list-keys --with-colons | awk -F: '$1 == "pub" && ($2 == "e" || $2 == "r") { print $5 }' | xargs gpg --no-default-keyring --keyring ${TMPDIR}/keyring.gpg --batch --yes --delete-keys

echo2 "Generating recipient list"
# The code does not allow for sub-keys that support more than one function, e.g. sign and encrypt
RECIPS=`gpg --no-default-keyring --keyring ${TMPDIR}/keyring.gpg --list-keys --with-colons | awk -F: '$1 == "sub" && $12 == "e" { printf "-r %s ", $5 }'`

echo2 "Encrypting ${INPUTFILE} to ${OUTPUTFILE} using temporary keyring"
test "$INPUTFILE" == '-' && echo2 "No input file specified. Type your message to encrypt here, finish with Ctrl+D:"
gpg --no-default-keyring --quiet --keyring ${TMPDIR}/keyring.gpg ${RECIPS} --armor --trust-model always --output ${OUTPUTFILE} --encrypt ${INPUTFILE}

if [[ "$OUTPUTFILE" != '-' ]]; then
    echo2 "All done. Your encrypted message contains the following:"
    echo2 ""
    cat ${OUTPUTFILE}
    # This needs to be after the contents, which are generally large
    echo2 "Your encrypted message has been stored in ${OUTPUTFILE}"
else
    rm -rf ${TMPDIR} # no longer needed
fi
