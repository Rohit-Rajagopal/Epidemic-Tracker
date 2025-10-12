const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: {
        main: "./src/index.js",
        locations: "./src/js/locations.js"
    },
    output: {
        filename: "[name].js",
        path: path.resolve(__dirname, "dist"),
        clean: true,
    },
    plugins: [
        new HtmlWebpackPlugin ({
            template: "./src/index.html",
            filename: "index.html",
            chunks: ["main"],
        }),
        new HtmlWebpackPlugin ({
            template: "./src/html/locations.html",
            filename: "locations.html",
            chunks: ["locations"],
        }),
    ],
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: "asset/resource",
            },
            {
                test: /\.html$/i,
                loader: "html-loader",
            }
        ],
    },
};