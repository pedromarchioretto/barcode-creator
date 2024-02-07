from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)
@app.route('/create_tag', methods=["POST"])
def home():
  get_tag = request.json.get('product-tag')
  print(get_tag)
  barcode = Code128(get_tag, writer=ImageWriter())
  barcode.save(get_tag)

  return jsonify({'tag': get_tag})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
