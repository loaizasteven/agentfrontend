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

def change_button_style(widget_label, title, content):
    """ Modified from:
    https://discuss.streamlit.io/t/issues-with-background-colour-for-buttons/38723/2
    Args:
        widget_label
        title
        content
    """
    button_style = f"""
    <script>
        var elements = window.parent.document.querySelectorAll('button');
        for (var i = 0; i < elements.length; i++) {{
            if (elements[i].innerText == '{widget_label}') {{
                elements[i].style.padding = '7px';
                elements[i].style.margin = '0px';
                elements[i].style.borderRadius = '5px';
                elements[i].style.border = '1px solid #e0e0e0';
                elements[i].style.backgroundColor = '#f0f4f8';
                elements[i].innerHTML = '<span><h4 style="text-align: center; font-size: 15px;">✨{title}</h4><p style="text-align:left; font-size:11px;">{content}</p></span>';
            }}
        }}
    </script>
    """

    components.html(button_style, height=0, width=0)
    