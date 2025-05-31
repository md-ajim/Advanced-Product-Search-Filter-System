"use client";

import { Checkbox } from "@/components/ui/checkbox";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Slider } from "@/components/ui/slider";
import { ChevronDown, CircleDollarSign, Star, Tag } from "lucide-react";
import { useState } from "react";
const MIN_PRICE = 0;
const MAX_PRICE = 10000;

const CollapsibleFilters = ({
 HandelCategoryChange,
  setIsCategory,
 is_category,
  value,
  setValue,
  FilterProductUpdate,
  setRating,
  rating,
}) => {
  return (
    <div className="w-full max-w-xs px-1 divide-y-2">
      <PriceRangeFilter
        value={value}
        setValue={setValue}
        FilterProductUpdate={FilterProductUpdate}
      />
      <CategoryFilter
        HandelCategoryChange={ HandelCategoryChange}
           setIsCategory={    setIsCategory}
       is_category={   is_category}
      />
      <RatingFilter setRating={setRating} rating={rating}         FilterProductUpdate={FilterProductUpdate}  />
    </div>
  );
};

const PriceRangeFilter = ({ value, setValue, FilterProductUpdate }) => {
  const handleChange = (newValue) => {
    FilterProductUpdate();
    setValue(newValue);
  };

  return (
    <CollapsibleFilter title="Price Range" icon={CircleDollarSign}>
      <div className="flex justify-between space-x-4">
        <Input
          type="number"
          value={value.from}
          onChange={(e) =>
            handleChange({ from: +e.target.value, to: value.to })
          }
          className="w-20"
        />
        <Input
          type="number"
          value={value.to}
          onChange={(e) =>
            handleChange({ from: value.from, to: +e.target.value })
          }
          className="w-20"
        />
      </div>
      <Slider
        min={MIN_PRICE}
        max={MAX_PRICE}
        step={10}
        value={[value.from, value.to]}
        onValueChange={([from, to]) => handleChange({ from, to })}
        className="w-full mt-4 mb-3"
      />
    </CollapsibleFilter>
  );
};

function RatingFilter({ setRating, rating ,FilterProductUpdate  }) {
  // const [rating, setRating] = useState(null);
  const [hoveredRating, setHoveredRating] = useState(null);

  const handleClick = (ratingValue) => {
    const newRating = ratingValue === rating ? null : ratingValue;
    setRating(newRating);
    // FilterProductUpdate();  // Call API after rating is set
  };


  console.log(rating, 'rating');
  

  return (
    <CollapsibleFilter title="Rating" icon={Star}>
      <div className="flex space-x-1 mb-1">
        {[1, 2, 3, 4, 5].map((ratingValue) => (
          <Star
            key={ratingValue}
            className={`h-6 w-6 cursor-pointer ${
              (
                hoveredRating !== null
                  ? hoveredRating >= ratingValue
                  : rating !== null && rating >= ratingValue
              )
                ? "text-yellow-400 fill-yellow-400"
                : "text-gray-300"
            }`}
            onMouseEnter={() => setHoveredRating(ratingValue)}
            onMouseLeave={() => setHoveredRating(null)}
            onClick={() => handleClick(ratingValue)}
          />
        ))}
      </div>
    </CollapsibleFilter>
  );
}

const categories = [
  "ELECTRONICS",
  "CLOTHES",
  "HOME",
  "BEAUTY",
  "SPORTS",
];

const CategoryFilter = ({
   HandelCategoryChange,
     setIsCategory,
 is_category,
}) => {
  return (
    <CollapsibleFilter title="Category" icon={Tag}>
      {categories.map((category, index) => (
        <div
          key={index}
          onClick={() =>  HandelCategoryChange(category)}
          className="mb-2 flex items-center space-x-3"
        >
          <Checkbox id={category} checked={ is_category === category} />
          <Label htmlFor={category}>{category}</Label>
        </div>
      ))}
    </CollapsibleFilter>
  );
};

const CollapsibleFilter = ({ title, icon: Icon, children }) => (
  <Collapsible defaultOpen>
    <CollapsibleTrigger className="group flex w-full items-center justify-between py-3">
      <h3 className="flex items-center gap-2 text-sm font-semibold">
        {!!Icon && <Icon className="h-5 w-5" />} {title}
      </h3>
      <ChevronDown className="h-4 w-4 group-data-[state=open]:rotate-180 transition-transform text-muted-foreground" />
    </CollapsibleTrigger>
    <CollapsibleContent className="pt-1 pb-3">{children}</CollapsibleContent>
  </Collapsible>
);

export default CollapsibleFilters;
