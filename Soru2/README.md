# Soru2-BUTELEME: Laravel + MySQL Kullanıcı Kayıt API

## Servisler
- Laravel (port 8081)
- MySQL (port 3307)

## Kullanım
```
docker-compose up --build
```

## API Testi
```
curl -X POST http://localhost:8081/api/register \
-H "Content-Type: application/json" \
-d '{"name": "Ali", "email": "ali@example.com", "password": "123456"}'
```
