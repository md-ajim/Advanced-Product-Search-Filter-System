export interface Category {
    id: number;
    name: "ALL" | "CLOTHES" | "HOME" | "ELECTRONICS" | "BEAUTY" | "SPORTS";
    title?: string | null;
}

export interface Product {
    id: number;
    name: string;
    title?: string | null;
    category?: Category | null;
    description: string;
    price: string; // Decimal as string to preserve precision
    size?: string | null;
    color?: string | null;
    image?: string | null;
    is_active: boolean;
    reviews: Review[] | null 
    created_at: string; // ISO date string
    updated_at: string; // ISO date string
}


export interface Review {
    product : string 
    rating : number
    created_at: string
}