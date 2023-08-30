from IPython.display import display, HTML

def display_dfs(dfs, gap: int = 50) -> None:
    html: str = ""
    
    for title, df in dfs.items():  
        df_html = df._repr_html_()
        cur_html = f'<div> <h3>{title}</h3> {df_html}</div>'
        html +=  cur_html

    html: str = f"""
    <div style="display:flex; gap:{gap}px; justify-content:center;">
        {html}
    </div>
    """
    
    display(HTML(html), raw=True)