const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const src = path.join(root, "site");
const dest = path.join(root, "public");

function copyRecursive(from, to) {
  const stat = fs.statSync(from);
  if (stat.isDirectory()) {
    fs.mkdirSync(to, { recursive: true });
    for (const name of fs.readdirSync(from)) {
      copyRecursive(path.join(from, name), path.join(to, name));
    }
    return;
  }
  fs.copyFileSync(from, to);
}

if (fs.existsSync(dest)) {
  fs.rmSync(dest, { recursive: true, force: true });
}
copyRecursive(src, dest);
console.log("Copied site/ -> public/ for Vercel static output");
