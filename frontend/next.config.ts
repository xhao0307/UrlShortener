/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        // 判断是否在Docker容器内运行
        destination: process.env.NODE_ENV === "production"
          ? "http://backend:8000/api/:path*" // 容器内部互访
          : "http://127.0.0.1:8000/api/:path*", // 本地浏览器访问
      },
    ];
  },
};

module.exports = nextConfig;