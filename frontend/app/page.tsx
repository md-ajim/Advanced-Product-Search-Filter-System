"use client";
import CollapsibleFilters from "@/components/collapsible-04";
import { StarIcon, EyeIcon, ShoppingCart, HeartIcon } from "lucide-react";
import Link from "next/link";
import { Skeleton } from "@/components/ui/skeleton";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";
import { useRouter, useParams, useSearchParams } from "next/navigation";
import PaginationDemo from "@/components/pagination/pagination";
const MIN_PRICE = 0;
const MAX_PRICE = 1000000;
export default function Home() {
  const [product, setProduct] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const productsPerPage = 7;
  const [is_category, setIsCategory] = useState([]);
  const searchParams = useSearchParams();
  const search_query = searchParams.get("search");
  const [rating, setRating] = useState(null);
  const [value, setValue] = useState({
    from: MIN_PRICE,
    to: MAX_PRICE,
  });

  const searchProductUpdate = async () => {
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
      setLoading(false);
    }
  };

  const FilterProductUpdate = async () => {
    setLoading(true);

    const params = {
      category: is_category,
      min_price: searchParams.get("min_price") || value.from,
      max_price: searchParams.get("max_price") || value.to,
      rating: searchParams.get("rating") || rating,
      // min_rating:searchParams.get('min_rating')|| '',
      // max_rating :searchParams.get('max_rating')|| '',
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
  };

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
  }, [search_query, rating, currentPage]);

  const HandelCategoryChange = async (category = []) => {
    setIsCategory(category);
    FilterProductUpdate();
  };

  return (
    <div className=" mt-4 bg-background   dark:border-slate-700/70 max-w-screen-xl mx-auto ">
      <main className="  grid md:grid-cols-4 grid-cols-1  place-content-center  md:px-0 lg:px-0 px-2 mb-4   gap-4">
        <div className=" flex   justify-center justify-items-center">
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

        {loading
          ? Array(3)
              .fill(0)
              .map((_, kye) => <SkeletonCard key={kye} />)
          : product.map((item, index) => (
              <div
                key={index}
                className="border border-solid md:h-[450px]  lg:h-[450px] md:p-0 pb-4 lg:p-0   w-full h-auto flex flex-col border-gray-300 rounded-lg shadow-sm hover:shadow-md"
              >
                <Link href={`/product/`}>
                  <figure className=" relative">
                    <img
                      className="w-full rounded-t-lg"
                      src={`${item.image}`}
                      width={300}
                      height={300}
                      alt={"ofrx"}
                    />
                    <Badge
                      variant="secondary"
                      className="absolute top-2 right-2 text-xs px-2 py-1 rounded-lg"
                    >
                      {item?.category?.name}
                    </Badge>
                  </figure>
                </Link>
                <div className="   border-t  px-4">
                  <div className="">
                    <div className="flex justify-between items-start">
                      <div>
                        <div className="flex items-center space-x-1 mt-1">
                          <div className="flex">
                            {[...Array(1, 5)].map((_, i) => (
                              <StarIcon
                                key={i}
                                className={`w-4 h-4 ${
                                  i < Math.floor(2)
                                    ? "text-yellow-500"
                                    : "text-gray-300"
                                }`}
                              />
                            ))}
                          </div>
                          <span className="text-sm text-gray-500">{5}</span>
                        </div>
                      </div>
                    </div>

                    <div className="flex justify-between items-center">
                      <p className="text-lg font-bold font-semibold">
                        {item.price}
                      </p>
                      <Badge className="bg-green-100 text-green-700 px-2 py-1 rounded-lg">
                        In Stock
                      </Badge>
                    </div>
                  </div>

                  <div className=" flex flex-col space-y-1">
                    <div className="flex justify-between items-center">
                      <input
                        type="number"
                        defaultValue={1}
                        className="border rounded-lg p-1 md:w-24 text-center"
                      />
                      <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.3 }}
                      >
                        <Button className="flex-1">
                          <ShoppingCart className="w-4 h-4 mr-2" />
                          Add to cart
                        </Button>
                      </motion.div>
                    </div>
                    <div className="flex items-center justify-between">
                      <Button variant="outline" className="w-1/2">
                        <HeartIcon className="mr-2 h-4 w-4" /> Wishlist
                      </Button>

                      <Button
                        variant="link"
                        className="w-1/2 text-sm text-black"
                      >
                        <Link
                          className="flex items-center gap-1"
                          href={`/product/`}
                        >
                          <EyeIcon className="h-4 w-4 underline" />
                          <span className=" dark:text-white">View Details</span>
                        </Link>
                      </Button>
                    </div>
                  </div>
                </div>
              </div>
            ))}
      </main>

      <div className=" flex justify-center items-center   w-full mx-auto  justify-items-center">
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
    <div className="border md:h-[400px] lg:h-[400px] w-full h-auto flex flex-col border-gray-300 rounded-lg shadow-sm">
      <Skeleton className="h-[200px] w-full rounded-t-lg" />
      <div className="p-2 space-y-2">
        <Skeleton className="h-5 w-3/4" />
        <Skeleton className="h-4 w-1/2" />
        <Skeleton className="h-6 w-1/4" />
        <div className="flex space-x-2">
          <Skeleton className="h-10 w-1/2 rounded-md" />
          <Skeleton className="h-10 w-1/2 rounded-md" />
        </div>
      </div>
    </div>
  );
}
