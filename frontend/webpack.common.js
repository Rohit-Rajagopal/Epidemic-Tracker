const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: {
        main: "./src/index.js",
        locations: "./src/js/locations.js",
        cluster: "./src/js/cluster.js",
        add_news: "./src/js/add_news.js",
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
        new HtmlWebpackPlugin ({
            template: "./src/html/cluster.html",
            filename: "cluster.html",
            chunks: ["cluster"],
        }),
        new HtmlWebpackPlugin ({
            template: "./src/html/add_news.html",
            filename: "add_news.html",
            chunks: ["add_news"],
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