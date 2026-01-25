#!/bin/bash

set -e

# Configurable variables
DB_USER="myuser"
DB_PASS="mypassword"
DB_NAME="mydb"
DATA_DIR="/var/lib/postgres/data"

echo "############################"
echo "🔧 Installing PostgreSQL..."
echo "############################"
sudo pacman -S --noconfirm postgresql


echo "############################"
echo "🛠 Initializing database cluster..."
echo "############################"
sudo -iu postgres initdb --locale "$LANG" -E UTF8 -D "$DATA_DIR"

echo "🚀 Enabling and starting PostgreSQL service..."
sudo systemctl enable --now postgresql

echo "👤 Creating PostgreSQL user and database..."
sudo -iu postgres psql <<EOF
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
CREATE DATABASE $DB_NAME OWNER $DB_USER;
EOF

echo "🔐 Adjusting pg_hba.conf to allow password authentication..."
PG_HBA="/var/lib/postgres/data/pg_hba.conf"
sudo sed -i "s/^host\s\+all\s\+all\s\+127.0.0.1\/32\s\+.*$/host    all             all             127.0.0.1\/32            md5/" "$PG_HBA"
sudo sed -i "s/^host\s\+all\s\+all\s\+::1\/128\s\+.*$/host    all             all             ::1\/128                 md5/" "$PG_HBA"

echo "🔄 Restarting PostgreSQL to apply changes..."
sudo systemctl restart postgresql

echo "✅ PostgreSQL is set up with:"
echo "   User:     $DB_USER"
echo "   Password: $DB_PASS"
echo "   Database: $DB_NAME"
echo ""
echo "🔗 Connection string:"
echo "   postgresql://$DB_USER:$DB_PASS@localhost:5432/$DB_NAME"

