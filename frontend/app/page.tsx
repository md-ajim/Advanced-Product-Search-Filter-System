"use client";
import Image from "next/image";
import CollapsibleFilters from "@/components/collapsible-04";
import { StarIcon, EyeIcon, ShoppingCart, HeartIcon } from "lucide-react";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { SkeletonCard } from "@/components/ui/skeleton";
import { buttonVariants } from "@/components/ui/button";

import {
  Pagination,
  PaginationContent,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";
import { useEffect, useState } from "react";
import { cn } from "@/lib/utils";
import { motion } from "framer-motion";
import axios from "axios";
import { useRouter, useParams, useSearchParams } from "next/navigation";
const MIN_PRICE = 0;
const MAX_PRICE = 10000;
export default function Home() {
  const [product, setProdcut] = useState([]);
  const [loading, setLoading] = useState(false);
  const [iscategorie, setIscategorie] = useState([]);
  const searchParams = useSearchParams();
  const search_quary = searchParams.get("search");
  const [rating, setRating] = useState(null);
  const [value, setValue] = useState({
    from: MIN_PRICE,
    to: MAX_PRICE,
  });

  const searchProductUpdate = async () => {
    setLoading(true);

    const params = {
      search: search_quary,
    };

    try {
      const response = axios.get(`http://127.0.0.1:8000/api/product/`, {
        params,
      });
      const data = (await response).data.results;

      if (!data) {
        alert(`Product is get field${data.errr}`);
        setProdcut([]);
      }
      setProdcut(data);
      return data;
    } catch (errr) {
      console.log(errr, "error");
      setProdcut([]);
    } finally {
      setLoading(false);
      console.log("get product error");
    }
  };

  useEffect(() => {
    const factProductData = async () => {
      setLoading(true);

      try {
        const response = axios.get(`http://127.0.0.1:8000/api/product/`);

        const data = (await response).data.results;

        if (!data) {
          alert(`Product is get field${data.errr}`);
        }
        setProdcut(data);
        return data;
      } catch (errr) {
        console.log(errr, "error");
      } finally {
        setLoading(false);
        console.log("get product error");
      }
    };

    if (search_quary !== null) {
      searchProductUpdate();
    }

    if (rating !== null) {
      FilterProductUpdate();
    } else {
      factProductData();
    }
  }, [search_quary, rating]);

  const FilterProductUpdate = async () => {
    setLoading(true);

    const params = {
      category: iscategorie,
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
        alert(`Product is get field${data.errr}`);
        setProdcut([]);
      }
      setProdcut(data);
      return data;
    } catch (errr) {
      console.log(errr, "error");
      setProdcut([]);
    } finally {
      setLoading(false);
      console.log("get product error");
    }
  };

  const handleCategorieChinge = async (categorie) => {
    setIscategorie(categorie);
    FilterProductUpdate();
  };

  return (
    <div className=" mt-24 bg-background   dark:border-slate-700/70 max-w-screen-xl mx-auto ">
      <main className="  grid md:grid-cols-4 grid-cols-1  place-content-center   mb-4   gap-4">
        <div className=" flex   justify-center justify-items-center">
          <CollapsibleFilters
            handleCategorieChinge={handleCategorieChinge}
            setIscategorie={setIscategorie}
            iscategorie={iscategorie}
            value={value}
            setValue={setValue}
            FilterProductUpdate={FilterProductUpdate}
            setRating={setRating}
            rating={rating}
          />
        </div>

          {loading
            ? "Loading..."
            : product.map((item, index) => (
                <div
                  key={index}
                  className="border border-solid md:h-[450px] lg:h-[450px] md:p-0 pb-4 lg:p-0   w-full h-auto flex flex-col border-gray-300 rounded-lg shadow-sm hover:shadow-md"
                >
                  <Link href={`/product/`}>
                    <figure className="relative">
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
                            <span className=" dark:text-white">
                              View Details
                            </span>
                          </Link>
                        </Button>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
      </main>

      <div className=" flex justify-center items-center   w-full mx-auto  justify-items-center">
        <Pagination>
          <PaginationContent>
            <PaginationItem>
              <PaginationPrevious href="#" />
            </PaginationItem>
            <PaginationItem>
              <PaginationLink href="#">1</PaginationLink>
            </PaginationItem>
            <PaginationItem>
              <PaginationLink
                href="#"
                isActive
                className={cn(
                  "!shadow-none hover:!text-primary-foreground",
                  buttonVariants({
                    variant: "default",
                    size: "icon",
                  })
                )}
              >
                2
              </PaginationLink>
            </PaginationItem>
            <PaginationItem>
              <PaginationLink href="#">3</PaginationLink>
            </PaginationItem>
            <PaginationItem>
              <PaginationNext href="#" />
            </PaginationItem>
          </PaginationContent>
        </Pagination>
      </div>
    </div>
  );
}
