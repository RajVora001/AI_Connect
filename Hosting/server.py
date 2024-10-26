import msgpack
import uvicorn
from model_handler import load_model, predict

model = load_model()


async def app(scoope, receive, send):
    assert scoope["type"] == "http"

    if scoope["path"] == "/predict" and scoope["method"] == "POST":
        body = await receive()
        input_data = msgpack.unpackb(body["body"])

        prediction = predict(model, input_data)

        response = {
            "type": "http.response.start",
            "status": 200,
            "headers": [(b"content-type", b"application/x-msgpack")],
        }
        await send(response)
        await send(
            {
                "type": "http.response.body",
                "body": msgpack.packb({"prediction": prediction}),
            }
        )

    else:
        await send(
            {
                "type": "http.response.start",
                "status": 404,
                "headers": [(b"content-type", b"text/plain")],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": b"Not Found",
            }
        )
        
if __name__=="__main__":
    uvicorn.run("hosting.server:app", host="0.0.0.0", port=5000)
