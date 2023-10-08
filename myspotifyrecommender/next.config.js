module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/index.py',
        destination: 'http://127.0.0.1:5328/:path*', // Proxy to Backend
      },
    ]
  },
}