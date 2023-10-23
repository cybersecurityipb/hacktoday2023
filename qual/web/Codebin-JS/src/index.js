const express = require("express");
const session = require("express-session");
const path = require("path");
const { v4 } = require("uuid");
const jwt = require("jsonwebtoken");
const secretKey = "SldUX1Rva2Vu";
const app = express();
const { LogInsCollection, ItemsCollection } = require("./mongo");
const port = process.env.PORT || 8989;

app.use(
  session({
    secret: "secretKey",
    resave: true,
    saveUninitialized: true,
  })
);

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

const tempelatePath = path.join(__dirname, "../tempelates");
const publicPath = path.join(__dirname, "../public");
console.log(publicPath);

const verifyToken = (req, res, next) => {
  const { naming, token } = req.session;

  if (!token && req.path !== "/login" && req.path !== "/signup") {
    return res.status(401).send("Access denied. No token provided.");
  }

  jwt.verify(token, secretKey, (err, decoded) => {
    if (err && req.path !== "/login" && req.path !== "/signup") {
      return res.status(403).send("Invalid token.");
    }

    req.decoded = decoded;
    next();
  });
};

app.set("view engine", "hbs");
app.set("views", tempelatePath);
app.use(express.static(publicPath));

app.get("/signup", (req, res) => {
  res.render("signup");
});

app.get("/", (req, res) => {
  res.render("login");
});

const flag = "agrihack0x08{c0nr4tul4t10n5_y0u_h4v3_4cc3ss3d_th3_fl4g_N1C33}";

app.get("/home", verifyToken, async (req, res) => {
  const { naming } = req.session;
  const { isAdmin } = await LogInsCollection.findOne({ name: naming });

  try {
    const allData = await ItemsCollection.find();
    res.render("home", { data: allData, naming, isAdmin, flag });
  } catch (error) {
    res.send("Error: " + error.message);
  }
});

app.post("/signup", async (req, res) => {
  const data = {
    name: req.body.name,
    password: req.body.password,
  };

  const checking = await LogInsCollection.findOne({ name: req.body.name });

  try {
    if (checking && checking.password === req.body.password) {
      return res.send("User details already exist");
    } else {
      await LogInsCollection.create(data);
    }
  } catch (error) {
    return res.send("Error: " + error.message);
  }

  const token = jwt.sign({ name: req.body.name }, secretKey);
  req.session.naming = req.body.name;
  req.session.token = token;
  req.session.isAdmin = false;
  res.redirect("/home");
});

app.post("/login", async (req, res) => {
  try {
    const { name, password, isAdmin } = req.body;
    const user = await LogInsCollection.findOne({ name });

    if (!user) {
      return res.send("User not found");
    }

    if (user.password !== password) {
      return res.send("Incorrect password");
    }

    const token = jwt.sign({ name }, secretKey);
    req.session.naming = name;
    req.session.token = token;

    if (isAdmin) {
      await LogInsCollection.updateOne({ name }, { $set: { isAdmin: true } });
    } else {
      await LogInsCollection.updateOne({ name }, { $set: { isAdmin: false } });
    }

    res.redirect("/home");
  } catch (error) {
    res.send("Error: " + error.message);
  }
});

app.post("/upload", async (req, res) => {
  const itemData = {
    title: req.body.title,
    description: req.body.description,
  };

  const { naming, token } = req.session;

  try {
    await ItemsCollection.create(itemData);
    res.redirect(
      `/home?naming=${encodeURIComponent(naming)}&token=${encodeURIComponent(
        token
      )}`
    );
  } catch (error) {
    res.send("Error: " + error.message);
  }
});

app.get("/edit/:itemId", verifyToken, async (req, res) => {
  const itemId = req.params.itemId;
  const { naming, token } = req.session;

  try {
    const item = await ItemsCollection.findById(itemId);
    res.render("edit", { item, naming, token });
  } catch (error) {
    res.send("Error: " + error.message);
  }
});

app.post("/update/:itemId", verifyToken, async (req, res) => {
  const itemId = req.params.itemId;
  const { title, description } = req.body;
  const { naming, token } = req.session;

  try {
    await ItemsCollection.findByIdAndUpdate(itemId, {
      title,
      description,
    });
    res.redirect(
      `/home?naming=${encodeURIComponent(naming)}&token=${encodeURIComponent(
        token
      )}`
    );
  } catch (error) {
    res.send("Error: " + error.message);
  }
});

app.post("/delete/:itemId", verifyToken, async (req, res) => {
  const itemId = req.params.itemId;
  const { naming, token } = req.session;

  try {
    await ItemsCollection.findByIdAndRemove(itemId);
    res.redirect(
      `/home?naming=${encodeURIComponent(naming)}&token=${encodeURIComponent(
        token
      )}`
    );
  } catch (error) {
    res.send("Error: " + error.message);
  }
});

app.post("/logout", async (req, res) => {
  const { naming } = req.session;

  await LogInsCollection.updateOne(
    { name: naming },
    { $set: { isAdmin: false } }
  );

  req.session.destroy();
  res.redirect("/");
});

app.listen(port, "0.0.0.0", () => {
  console.log("Server listening on port", port);
});
