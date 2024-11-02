import streamlit as st
import streamlit.components.v1 as components

def hide_header_footer() -> None:
    hide_style = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top; 0rem;}
    </style>
    """

    components.html(hide_style)

def detect_browser():
    detect_script="""
        <html>
            <head>
                <title>Browser Detection</title>
            </head>
            <body>
                <p id="browser-info"></p>

                <script>
                    var isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
                    var isSafari = /Safari/.test(navigator.userAgent) && /Apple Computer/.test(navigator.vendor);

                    var browserInfo = document.getElementById("browser-info");

                    if (isChrome) {
                        console.log("You are using Chrome");
                    } else if (isSafari) {
                        browserInfo.innerText = "You are using Safari, consider switching to Chrome for better experience";
                    }
                </script>
            </body>
        </html>
    """
    components.html(detect_script)

def change_button_style(widget_label:str, title:str, content:str) -> None:
    """ Modified from:
    https://discuss.streamlit.io/t/issues-with-background-colour-for-buttons/38723/2
    Args:
        widget_label
        title: max limit 21 characters
        content: max limit 86 characters
    """
    tlimit = 21
    climit = 86
    assert len(title) <= tlimit and len(content) <= climit, 'Button Content Exceeds Max Limit'

    # Pad parameters with white space for uniform button shape when window size changes
    # TODO: Additional work needed to preserve button size
    button_style = f"""
    <script>
        var elements = window.parent.document.querySelectorAll('button');
        for (var i = 0; i < elements.length; i++) {{
            if (elements[i].innerText == '{widget_label}') {{
                elements[i].style.padding = '7px';
                elements[i].style.margin = '0px';
                elements[i].style.height = '100px';
                elements[i].style.borderRadius = '5px';
                elements[i].style.border = '1px solid #e0e0e0';
                elements[i].style.backgroundColor = '#f0f4f8';
                elements[i].innerHTML = '<span><h4 style="text-align: left; font-size: 15px; white-space:pre-wrap;">✨{title.ljust(tlimit)}</h4><p style="text-align:left; font-size:11px; white-space:pre-wrap;">{content.ljust(climit)}</p></span>';
            }}
        }}
    </script>
    """

    components.html(button_style, height=0, width=0)
    