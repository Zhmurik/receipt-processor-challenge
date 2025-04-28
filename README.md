# How to build and test

1. Clone repo by running `git clone https://github.com/fetch-rewards/receipt-processor-challenge.git`
2. Build docker image `docker build -t apichallenge .`
3. Run docker container `docker run -p 8000:8000 apichallenge`
4. Test APIs with preferred tool, example
   - a. POST `http://0.0.0.0:8000/receipts/process/`
   - b. GET `http://0.0.0.0:8000/receipts/f957bc2a-ade5-43cb-b4be-9d4a1d7b8d7c/points`


