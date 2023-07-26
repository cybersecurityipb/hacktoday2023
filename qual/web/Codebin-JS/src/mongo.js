const mongoose = require("mongoose");

mongoose.set("strictQuery", false);
mongoose
  .connect("mongodb://mongo:27017/LoginForm")
  .then(() => {
    console.log("mongoose connected");
  })
  .catch((e) => {
    console.log("failed to connect the Mongodb");
  });

const logInSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
  token: {
    type: String,
  },
  isAdmin: {
    type: Boolean,
    default: false,
  },
});

const itemSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
});

const LogInsCollection = mongoose.model("LoginData", logInSchema);
const ItemsCollection = mongoose.model("ItemData", itemSchema);

module.exports = { LogInsCollection, ItemsCollection };
