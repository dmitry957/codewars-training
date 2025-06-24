def get_first_python(users):
python_dev = next((dev for dev in users if dev['language'] == 'Python'), None)
return f"{python_dev['first_name']}, {python_dev['country']}" if python_dev else 'There will be no Python developers'