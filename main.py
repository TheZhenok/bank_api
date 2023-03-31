from app import FastAPIApp


app: FastAPIApp = FastAPIApp()

@app.get('/', response_model=dict[str, str])
def main_page():
    return {"message": "hello"}
