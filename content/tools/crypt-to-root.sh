#!/usr/bin/bash
if [[ "$1" == "-h" ]]; then
    echo "Usage: crypt-to-root.sh [\$FILE-TO-ENCRYPT]"
    echo "e.g.: crypt-to-root.sh foo.txt"
    echo "use crypt-to-root.sh without any arguments to encrypt from stdin instead"
    exit 0
fi

cmd_exists()
{
    command -v "$1" >/dev/null 2>&1
}

# Ensure we have gpg, awk, and mktemp
if ! cmd_exists gpg ; then
    echo "This tool needs the gpg executable in order to work. Please install it!"
    exit 1
fi
if ! cmd_exists awk ; then
    echo "This tool needs the awk executable in order to work. Please install it!"
    exit 1
fi
if ! cmd_exists mktemp; then
    echo "This tool needs the mktemp executable in order to work. Please install it!"
    exit 1
fi

KEYSURL="https://infra.apache.org/tools/infrastructure-root.asc"
KEYSFILE="KEYS.asc"
INPUTFILE=$1
TMPDIR=`mktemp -d`
OUTPUTFILE="${TMPDIR}/${INPUTFILE}.asc"

# If no filename is specified, read from stdin instead
if [[ -z "$INPUTFILE" ]]; then
   INPUTFILE="${TMPDIR}/message.txt"
   OUTPUTFILE="${INPUTFILE}.asc"
   echo "No input file specified. Type your message to encrypt here, finish with Ctrl+D:"
   while IFS= read -r line; do
       echo "$line" >> ${INPUTFILE}
   done
fi


echo "Downloading ${KEYSURL}"
wget ${KEYSURL} -O ${TMPDIR}/${KEYSFILE}

echo "Importing ${KEYSFILE} into ${TMPDIR}/keyring.gpg"
gpg --no-default-keyring --quiet --keyring ${TMPDIR}/keyring.gpg --import ${TMPDIR}/${KEYSFILE}

echo "Removing any expired or revoked keys"
gpg --no-default-keyring --quiet --keyring ${TMPDIR}/keyring.gpg --list-keys --with-colons | awk -F: '$1 == "pub" && ($2 == "e" || $2 == "r") { print $5 }' | xargs gpg --no-default-keyring --keyring ${TMPDIR}/keyring.gpg --batch --yes --delete-keys

echo "Generating recipient list"
RECIPS=`gpg --no-default-keyring --keyring ${TMPDIR}/keyring.gpg --list-keys --with-colons | awk -F: '$1 == "sub" && ($12 == "e") { printf "-r %s ", $5 }'`

echo "Encrypting ${INPUTFILE} to ${OUTPUTFILE} using temporary keyring"
gpg --no-default-keyring --quiet --keyring ${TMPDIR}/keyring.gpg ${RECIPS} --armor --trust-model always --output ${OUTPUTFILE} --encrypt ${INPUTFILE}

echo "All done. Your encrypted message has been stored in ${OUTPUTFILE}, and contains the following:"
echo ""
cat ${OUTPUTFILE}
