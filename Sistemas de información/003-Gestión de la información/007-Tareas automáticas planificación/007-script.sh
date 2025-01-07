#!/bin/bash

# MySQL credentials
DB_USER="futbol"
DB_PASSWORD="futbol"
DB_NAME="futbol"

# Current timestamp in epoch format
TIMESTAMP=$(date +%s)

# Output filename with timestamp
DUMP_FILE="futbol_dump_${TIMESTAMP}.sql"

# Run the mysqldump command
mysqldump -u $DB_USER -p$DB_PASSWORD $DB_NAME > $DUMP_FILE

# Check if the dump was successful
if [ $? -eq 0 ]; then
    echo "Backup successful: $DUMP_FILE"
else
    echo "Backup failed."
    exit 1
fi
