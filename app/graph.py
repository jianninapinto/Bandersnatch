from altair import Chart, Tooltip, Title
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """
    Create a customized scatter plot chart to visualize the relationships between variables and groups.

    :arg:
        df (pandas.DataFrame): DataFrame containing all the monsters and their respective attributes.
        x (str): Name of the independent variable that is being plotted on the x-axis. This variable represents the
            horizontal axis in the scatter plot.
        y (str): Name of the dependent variable that is being plotted on the y-axis. This variable represents the
            vertical axis in the scatter plot.
        target (str): Name of the grouping variable for color encoding. This variable determines the hue
            of the data points in the scatter plot, indicating different groups or categories.

    :return:
        altair.Chart: Scatter plot chart representing the relationships between the variables and groups.
    """
    # Create a Chart object and assign it to the variable `graph`
    graph = Chart(
        data=df,
        title=Title(
            f"{y} by {x} for {target}",  # Dynamic title based on variables
            color="rgb(170,170,170)",
            fontSize=25,
            fontWeight="bold",
            offset=50)
    ).mark_circle(
        size=100
    ).encode(
        x=x,  # Map x variable to the x-axis
        y=y,  # Map y variable to the y-axis
        color=target,  # Map target variable to the color encoding
        tooltip=Tooltip(df.columns.to_list())  # Add tooltips based on DataFrame's column names
    ).properties(
        width=400,
        height=450,
        background="rgb(37,37,37)",
        padding=50
    ).configure_legend(
        titleColor="rgb(170,170,170)",
        labelColor="rgb(170,170,170)",
        padding=10
    ).configure_axis(
        gridColor="rgb(46,46,46)",
        titleColor='rgb(170,170,170)',
        labelColor="rgb(170,170,170)",
        titlePadding=10
    )
    # Return the completed scatter plot chart
    return graph
