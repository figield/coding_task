from flask import Flask, render_template, request

app = Flask(__name__)

min_value = 0
max_value = 1000


def calculate_guess_value(max_number, min_number):
    return (max_number - min_number) // 2 + min_number


@app.route("/guess", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return render_template("start_game_guess.html", min_value=min_value, max_value=max_value)
    else:  # POST
        is_win = "no"
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        old_guess_number = calculate_guess_value(max_number, min_number)
        answer = request.form.get("user_answer")
        if answer == "too big":
            max_number = old_guess_number
        elif answer == "too small":
            min_number = old_guess_number
        elif answer == "you win":
            is_win = "yes"

        new_guess = calculate_guess_value(max_number, min_number)
        return render_template("next_guess.html", min_value=min_number, max_value=max_number,
                               guess=new_guess, win=is_win)


if __name__ == '__main__':
    app.run()
