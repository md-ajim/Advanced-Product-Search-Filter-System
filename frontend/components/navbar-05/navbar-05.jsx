"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Logo } from "./logo";
import { Search } from "lucide-react";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
const Navbar05Page = () => {
  const [search, setSearch] = useState("");
  const router = useRouter();

  useEffect(() => {
    if (search === "") {
      router.push(`/`);
    }
  }, [search]);

  const handleSearchSubmit = async (e) => {
    e.preventDefault(); 
    console.log(e, "e");

    router.push(`/?search=${search}`);
  };

  return (
    <div className="">
      <nav className=" top-2 inset-x-4 h-16 bg-background border dark:border-slate-700/70 w-full max-w-screen-2xl  px-2 sm:px-4 lg:px-6 mx-auto  rounded-2xl">
        <div className="h-full flex items-center justify-between mx-auto px-4">
          <div className="flex items-center gap-2 md:gap-6">
           <Link href={'/'}>
            <Logo className="shrink-0" />
           </Link>

            <form onSubmit={handleSearchSubmit}>
              <div className="relative  hidden md:block">
                <Search className="h-5 w-5 hidden md:block absolute inset-y-0 my-auto left-2.5" />
                <Input
                  type="text"
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  className="pl-10 flex-1 hidden md:block bg-slate-100/70 dark:bg-slate-800 border-none shadow-none md:w-[280px] rounded-full"
                  placeholder="Search"
                />
              </div>
            </form>
          </div>

          <div className="flex items-center gap-2">
            <Button
              size="icon"
              className="bg-muted text-foreground hover:bg-accent shadow-none rounded-full md:hidden"
            >
              <Search className="!h-5 !w-5" />
            </Button>
            <Button
              variant="outline"
              className="hidden sm:inline-flex rounded-full"
            >
              Sign In
            </Button>
            <Button className="rounded-full">Get Started</Button>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Navbar05Page;
