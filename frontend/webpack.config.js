const path = require("path")
// const HtmlWebpackPlugin = require("html-webpack-plugin")

module.exports = {
    mode: "development",
    cache: true,
    entry: path.resolve(__dirname, "src/app.tsx"),
    output: {
        path: path.resolve(__dirname, "static/dist/"),
        filename: "application.js",
    },
    resolve: {
        modules: [
            path.resolve("./src"),
            path.resolve("./node_modules")
        ],
        extensions:[".js", ".ts", ".tsx"],
    },
    module: {
        rules: [
            {
                test: [/\.ts$/, /\.tsx$/,],
                use: [
                    {loader: "babel-loader"},
                    {loader:"ts-loader"},
                ],
            },
            {
                test: [/\.(png|jpe?g|gif|svg)$/i,],
                use: [
                    {
                        loader: "file-loader",
                        options:{
                            name:'[path][name].[ext]',//
                        },
                    },
                ],
            }
        ],
    },
}