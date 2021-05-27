Adilet Assabay, Anarbay Sanzhar, Aidaraly Yernur

- Pneumonia recognition with high accuracy using by CNN ML


#Installation of Webapp

- git clone https://github.com/sanzharanarbay/pneumoniaRecognition.git 
- copy .env.example .env 
- composer install && then composer update
- Create postgresql DB named "clinicsystem"
- php artisan key:generate
- php atisan cache:clear
- php artisan config:clear	
- php artisan migrate
- php artisan db:seed
- php artisan serve --port=3000
- Application is now running on port 3000
- link localhost:3000


# Admin
- admin@gmail.com - login , password - admin123