import json

def get_chart_data(chart_name):
    """
    Here's where you would talk to the data source! You'd grab the
    data and format it into a chart here. This might be in some columnar
    format, or some other json format.
    """
    chart_data = [
                  ("Bakersfield Central", "880000"),
                  ("Garden Groove harbour", "730000"),
                  ("Los Angeles Topanga", "590000"),
                  ("Compton-Rancho Dom", "520000"),
                  ("Daly City Serramonte", "330000")
                 ]
    return chart_data


def format_chart(chart_name, chart_data):
    chart = {
             "chart": {
                       "caption": "Harry's SuperMart",
                       "subCaption": "Top 5 stores in last month by revenue",
                       "numberPrefix": "$",
                       "theme": "carbon"
                      },
             "data": [{"label": label, "value": value} for label, value in chart_data]
            }
    return chart


def get_chart(chart_name):
    chart_data = get_chart_data(chart_name)
    chart = format_chart(chart_name, chart_data)
    return chart
