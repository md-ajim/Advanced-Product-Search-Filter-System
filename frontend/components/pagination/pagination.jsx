import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";
import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";
const PaginationDemo = ({ currentPage, totalPages, onPageChange }) => {
  let maxPageButtons = 4;

  let pageNumber = [];

  if (maxPageButtons < totalPages) {
    pageNumber = Array.from({ length: totalPages }, (_, i) => i + 1);
  } else {
    if (currentPage <= 3) {
      pageNumber = [1, 2, 3, "...", totalPages];
    } else if (currentPage >= totalPages - 2) {
      pageNumber = [
        1,
        "...",
        totalPages - 3,
        totalPages - 2,
        totalPages - 1,
        totalPages,
      ];
    } else {
      pageNumber = [
        1,
        "...",
        currentPage - 1,
        currentPage,
        currentPage + 1,
        "...",
        totalPages,
      ];
    }
  }

  return (
    <div className=" flex justify-center items-center   w-full mx-auto  justify-items-center">
      <Pagination>
        <PaginationContent>
          <PaginationItem>
            <PaginationPrevious
              href="#"
              onClick={() => onPageChange(Math.max(currentPage - 1, 1))}
              disabled={currentPage === 1}
            />
          </PaginationItem>

          {pageNumber.map((page, index) =>
            page === "..." ? (
              <PaginationEllipsis key={`ellipsis-${index}`} />
            ) : (
              <PaginationLink
                key={`page-${index}`}
                onClick={() => onPageChange(page)}
                isActive={currentPage === page}
              >
                {page}
              </PaginationLink>
            )
          )}

          <PaginationItem>
            <PaginationNext
              href="#"
              onClick={() => onPageChange(Math.max(currentPage + 1))}
              disabled={currentPage === totalPages}
            />
          </PaginationItem>
        </PaginationContent>
      </Pagination>
    </div>
  );
};

export default PaginationDemo;

// <PaginationItem>
//         <PaginationLink
//           href="#"
//           isActive
//           className={cn(
//             "!shadow-none hover:!text-primary-foreground",
//             buttonVariants({
//               variant: "default",
//               size: "icon",
//             })
//           )}
//         >
//           2
//         </PaginationLink>
//       </PaginationItem>
