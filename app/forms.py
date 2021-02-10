
class JoinRoomForm(FlaskForm):
    code = TextField("4-character room code", validators = [DataRequired()], Length(min=4, max=4))
    submit = SubmitField("submit")
