module.exports = {
  async rewrites() {
    return process.env.NODE_ENV === "development"
      ? [{ source: "/api/proxy", destination: "http://localhost:8000/question" }]
      : [];
  }
};
