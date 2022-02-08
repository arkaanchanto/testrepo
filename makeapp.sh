cd ./apps/
mkdir $1
cd ..
chmod +x manage.py
python manage.py startapp $1 apps/$1