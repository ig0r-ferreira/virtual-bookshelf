from flask_wtf import FlaskForm
from wtforms.fields import DecimalField, StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class CustomDecimalField(DecimalField):
    def __init__(
        self, label=None, validators=None, places=..., rounding=None, **kwargs
    ):
        self.widget.step = kwargs.pop('step', 'Any')
        super().__init__(label, validators, places, rounding, **kwargs)


class AddBook(FlaskForm):
    book_title = StringField('Book Title', validators=[InputRequired()])
    book_author = StringField('Book Author', validators=[InputRequired()])
    book_rating = CustomDecimalField(
        'Book Rating',
        validators=[InputRequired(), NumberRange(min=0, max=10)],
        step='0.1',
    )
    submit_btn = SubmitField('Save')
    cancel_btn = SubmitField('Cancel')


class EditBook(AddBook):
    book_title = StringField('Book Title', render_kw={'readonly': True})
    book_author = StringField('Book Author', render_kw={'readonly': True})
