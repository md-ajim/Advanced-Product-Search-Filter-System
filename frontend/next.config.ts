import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  images: {
    remotePatterns:[
      {
        protocol: 'https',
        hostname:'advanced-product-search-filter-system.onrender.com',
        port: '',
        pathname: '/media/images/**',
      },
    ],
  },
};

export default nextConfig;
