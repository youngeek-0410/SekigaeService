const path = require("path")
const getEntries = require("./lib/getEntries.js")

const entries = getEntries("./src/pages/")

module.exports = {
    mode: "development",
    cache: true,
    entry: entries,
    output: {
        path: path.resolve(__dirname, "dist/"),
        filename: "[name].bundle.js",
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