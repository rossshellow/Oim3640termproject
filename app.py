from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    result = None
    if request.method == 'POST':
        result = calculate_compound_interest(
            p=int(request.form['principal']),
            i=str(request.form['stock']),
            t=int(request.form['frequency']),
            n=int(request.form['years'])
        )
    # Pass the result to the front end
    return render_template('userform.html', result=result)


def calculate_compound_interest(p: int, i: float, t: int, n: int):
    """
    Calculate compound interest.

    :param p: The principal investment amount.
    :param i: The annual interest rate (decimal form). In this case, we based interest rate of each stock index based on average historical data.
    :param t: Number of years the money is invested for.
    :param n: Number of times that interest is compounded per year.
    :return: The future value of the investment.
    """
    if i == "VOO":
        i = .10
    elif i == "QQQ":
        i = .13
    elif i == "VTI":
        i = .0979
    elif i == "SPY":
        i = .10
    return p * ((1 + (i / t)) ** (n * t))


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
