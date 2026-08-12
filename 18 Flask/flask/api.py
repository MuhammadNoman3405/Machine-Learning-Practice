from flask import Flask,request,jsonify
app=Flask(__name__)

#Initial Data in my to-do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def welcome():
    return f"Welcome to the TO DO list"

# Get all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# get specific item viva id number

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'item not found'})
    return jsonify(item)

# put request creating the new itemss

@app.route('/items/<int:item_id>',methods=['POST'])
def create_item(item_id):
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'There is an error'})
    new_item={
        'id':items[-1]['id'] + 1 if items else 1,
        'name':request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# Put method
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'there is an error'})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

# Delete items
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    return jsonify({'result':'Item deleted successfully'})

if __name__==('__main__'):
    app.run(debug=True)