"use client";
import CollapsibleFilters from "@/components/collapsible-04";
import { StarIcon, EyeIcon, ShoppingCart, HeartIcon } from "lucide-react";
import Link from "next/link";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { useCallback } from "react";

import { Button } from "@/components/ui/button";
import { Product } from "@/types/product";
import Image from "next/image";
import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";
import { useSearchParams } from "next/navigation";
import PaginationDemo from "@/components/pagination/pagination";

const MIN_PRICE = 0;
const MAX_PRICE = 1000;

export default function Home() {
  const [product, setProduct] = useState<Product[]>([]);
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const productsPerPage = 10;
  const [is_category, setIsCategory] = useState([]);
  const searchParams = useSearchParams();
  const search_query = searchParams.get("search");
  const [rating, setRating] = useState(null);
  const [value, setValue] = useState({
    from: MIN_PRICE,
    to: MAX_PRICE,
  });

  const searchProductUpdate = useCallback(
    async () => {
      setLoading(true);
      try {
        const response = axios.get(
          `http://127.0.0.1:8000/api/product/?search=${search_query}`
        );
        const data = (await response).data.results;

        if (!data) {
          alert(`Product is get field${data.error}`);
          setProduct([]);
          console.log(data, "print error data");
        }
        setProduct(data);
        return data;
      } catch (error) {
        console.log(error, "error");
        setProduct([]);
      } finally {
        setLoading(false);
      }
    }, [search_query]
  )

  const FilterProductUpdate = useCallback(
    async () => {
      setLoading(true);
      const params = {
        category: is_category,
        min_price: searchParams.get("min_price") || value.from,
        max_price: searchParams.get("max_price") || value.to,
        rating: searchParams.get("rating") || rating,
      };

      try {
        const response = axios.get(`http://127.0.0.1:8000/api/product/`, {
          params,
        });
        const data = (await response).data.results;
        console.log(data, "data");

        if (!data) {
          alert(`Product is get field${data.error}`);
          setProduct([]);
        }
        setProduct(data);
        return data;
      } catch (error) {
        console.log(error, "error");
        setProduct([]);
      } finally {
        setLoading(false);
        console.log("filter function");
      }
    }, [is_category, value, rating, searchParams]
  )

  useEffect(() => {
    const factProductData = async () => {
      setLoading(true);
      try {
        const response = axios.get(
          `http://127.0.0.1:8000/api/product/?page=${currentPage}&page_size=${productsPerPage}`
        );
        setTotalPages(Math.ceil((await response).data.count / productsPerPage));
        const data = (await response).data.results;

        if (!data) {
          alert(`Product is get field${data.error}`);
        }
        setProduct(data);
        return data;
      } catch (error) {
        console.log(error, "error");
      } finally {
        setLoading(false);
        console.log("get function");
      }
    };

    if (search_query !== null) {
      searchProductUpdate();
    } else if (rating !== null) {
      FilterProductUpdate();
    } else {
      factProductData();
    }
  }, [search_query, rating, currentPage, searchProductUpdate, FilterProductUpdate]);

  const HandelCategoryChange = async (category = []) => {
    setIsCategory(category);
    FilterProductUpdate();
  };

  return (
    <div className="mt-4 bg-background dark:border-slate-700/70 w-full max-w-screen-2xl mx-auto px-2 sm:px-4 lg:px-6">
      <main className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6 mb-8">
        {/* Filter Sidebar - Full width on mobile, fixed position on desktop */}
        <div className="col-span-full lg:col-span-1 lg:sticky lg:top-4 lg:self-start">

            <CollapsibleFilters
              HandelCategoryChange={HandelCategoryChange}
              setIsCategory={setIsCategory}
              is_category={is_category}
              value={value}
              setValue={setValue}
              FilterProductUpdate={FilterProductUpdate}
              setRating={setRating}
              rating={rating}
            />
      
        </div>

        {/* Product Grid - Responsive columns */}
        <div className="col-span-full lg:col-span-3 grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-4 md:gap-6">
          {loading
            ? Array(6)
              .fill(0)
              .map((_, key) => <SkeletonCard key={key} />)
            : product.map((item, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: index * 0.1 }}
                className="border border-solid flex flex-col border-gray-300 dark:border-gray-700 rounded-lg shadow-sm hover:shadow-lg transition-shadow duration-300 bg-white dark:bg-gray-800 overflow-hidden"
              >
                {/* Product Image */}
                <Link href={`/product/${item.id}`} className="block">
                  <figure className="relative aspect-square w-full overflow-hidden bg-gray-100 dark:bg-gray-700">
                    <Image
                      className="object-cover hover:scale-105 transition-transform duration-300"
                      src={item.image ?? "/placeholder.png"}
                      fill
                      sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
                      alt={item.title || item.name}
                      priority={index < 3}
                    />
                    <Badge
                      variant="secondary"
                      className="absolute top-2 right-2 text-xs px-2 py-1 rounded-lg backdrop-blur-sm"
                    >
                      {item?.category?.name}
                    </Badge>
                  </figure>
                </Link>

                {/* Product Details */}
                <div className="border-t dark:border-gray-700 p-3 sm:p-4 flex flex-col flex-1">
                  {/* Title */}
                  <Link href={`/product/${item.id}`}>
                    <h3 className="text-sm sm:text-base font-semibold mb-2 line-clamp-2 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
                      {item.title || item.name}
                    </h3>
                  </Link>

                  {/* Rating */}
                  <div className="flex items-center gap-2 mb-2">
                    <div className="flex">
                      {[...Array(5)].map((_, i) => (
                        <StarIcon
                          key={i}
                          className={`w-3 h-3 sm:w-4 sm:h-4 ${item.reviews && item.reviews.length > 0 && i < item.reviews[0].rating
                              ? "text-yellow-500 fill-yellow-500"
                              : "text-gray-300 dark:text-gray-600"
                            }`}
                        />
                      ))}
                    </div>
                    <span className="text-xs sm:text-sm bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300">
                      ({item.reviews && item.reviews.length > 0 && item.reviews[0].rating})
                    </span>
                  </div>

                  {/* Price and Stock */}
                  <div className="flex justify-between items-center mb-3">
                    <p className="text-lg sm:text-xl font-bold text-gray-900 dark:text-white">
                      ${parseFloat(item.price).toFixed(2)}
                    </p>
                    <Badge className="bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300 text-xs px-2 py-1 rounded-lg">
                      {item.is_active ? "In Stock" : "Out of Stock"}
                    </Badge>
                  </div>

                  {/* Actions */}
                  <div className="flex flex-col gap-2 mt-auto">
                    {/* Quantity and Add to Cart */}
                    <div className="flex gap-2 items-center">
                      <input
                        type="number"
                        defaultValue={1}
                        min={1}
                        className="border dark:border-gray-600 rounded-lg p-2 w-16 sm:w-20 text-center text-sm dark:bg-gray-700 dark:text-white focus:ring-2 focus:ring-blue-500 focus:outline-none"
                      />
                      <Button
                        className="flex-1 text-xs sm:text-sm h-9 sm:h-10"
                        disabled={!item.is_active}
                      >
                        <ShoppingCart className="w-3 h-3 sm:w-4 sm:h-4 mr-1 sm:mr-2" />
                        <span className="hidden sm:inline">Add to cart</span>
                        <span className="sm:hidden">Add</span>
                      </Button>
                    </div>

                    {/* Wishlist and View Details */}
                    <div className="flex gap-2">
                      <Button
                        variant="outline"
                        className="flex-1 text-xs sm:text-sm h-9 sm:h-10"
                      >
                        <HeartIcon className="w-3 h-3 sm:w-4 sm:h-4 mr-1 sm:mr-2" />
                        <span className="hidden sm:inline">Wishlist</span>
                        <span className="sm:hidden">Save</span>
                      </Button>

                      <Button
                        variant="outline"
                        className="flex-1 text-xs sm:text-sm h-9 sm:h-10"
                        asChild
                      >
                        <Link href={`/product/${item.id}`}>
                          <EyeIcon className="w-3 h-3 sm:w-4 sm:h-4 mr-1 sm:mr-2" />
                          <span className="hidden sm:inline">View Details</span>
                          <span className="sm:hidden">View</span>
                        </Link>
                      </Button>
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
        </div>
      </main>

      {/* Pagination */}
      <div className="flex justify-center items-center w-full mx-auto pb-8">
        <PaginationDemo
          currentPage={currentPage}
          totalPages={totalPages}
          onPageChange={setCurrentPage}
        />
      </div>
    </div>
  );
}

function SkeletonCard() {
  return (
    <div className="border border-gray-300 dark:border-gray-700 flex flex-col rounded-lg shadow-sm overflow-hidden bg-white dark:bg-gray-800">
      <Skeleton className="aspect-square w-full" />
      <div className="p-3 sm:p-4 space-y-3">
        <Skeleton className="h-4 sm:h-5 w-3/4" />
        <Skeleton className="h-3 sm:h-4 w-1/2" />
        <Skeleton className="h-5 sm:h-6 w-1/4" />
        <div className="flex gap-2">
          <Skeleton className="h-9 sm:h-10 w-16 sm:w-20 rounded-md" />
          <Skeleton className="h-9 sm:h-10 flex-1 rounded-md" />
        </div>
        <div className="flex gap-2">
          <Skeleton className="h-9 sm:h-10 w-1/2 rounded-md" />
          <Skeleton className="h-9 sm:h-10 w-1/2 rounded-md" />
        </div>
      </div>
    </div>
  );
}