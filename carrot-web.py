from flask import Flask, render_template, request, send_file
from flask_wtf.csrf import CSRFProtect
from forms import InputForm
from carrot import generate_image
from os import environ
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)
app.secret_key = environ.get('flask_secret') or 'testing'
csrf = CSRFProtect()


def convert_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'png')
    img_io.seek(0)
    img_data = str(b64encode(img_io.getvalue()), 'utf8')
    img_src = f'data:image/png;base64,{img_data}'
    return img_src


@app.route("/", methods=['GET', 'POST'])
def main():
    form = InputForm(request.form)
    if form.validate_on_submit():
        contributors = [(form.name_1.data, form.val_1.data),
                        (form.name_2.data, form.val_2.data),
                        (form.name_3.data, form.val_3.data),
                        (form.name_4.data, form.val_4.data)]
        carrot_image = generate_image(contributors)
        return render_template('carrot.html', form=form, img_src=convert_pil_image(carrot_image))
    print(form.errors)
    return render_template('carrot.html', form=form, img_src=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')
