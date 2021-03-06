from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    post_id = HiddenField('Post ID',validators=[DataRequired()])
    comment_text = StringField('Comment text:', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Send', render_kw={"class": "btn btn-primary"})

class DeleteForm(FlaskForm):
    id_ = HiddenField("Content id", validators=[DataRequired()])

class PostAddForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"class":"form-control"})
    url  = StringField('pic url', render_kw = {"class":"form-control"})
    tag = StringField("Tag", render_kw={"class":"form-control"})
    text = TextAreaField("Text:", render_kw = {"class":"form-control"})
    submit = SubmitField("Send post!", render_kw={"class":"btn btn-primary"})
