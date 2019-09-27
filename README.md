# auto-workshop
Automotive service management system.


## How to develop?

1. Clone the repository.
2. Create the virtualenv with python 3.7.2.
3. Activate the virtualenv.
4. Install the dependencies.
5. Setup the instance with .env
6. Run the tests.


```console
git clone https://github.com/jrenato7/auto-workshop.git auto-workshop
cd auto-workshop
python -m venv .auto-workshop
source .auto-workshop/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```