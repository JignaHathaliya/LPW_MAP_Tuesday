docker build -t hms-image .
docker run -d -p 8000:8000 hms-image
docker login
docker tag hms-image yourusername/hms-image:latest
docker push yourusername/hms-image:latest
git init
git add .
git commit -m "Initial commit of Hospital Management System"
git remote add origin https://github.com/JignaHathaliya/LPW_MAP_Tuesday.&t/Hathaliya/hms.git
git push -u origin main