import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "#KostasVisualizations",
  description: "Interactive visual explanations for projective geometry, optimization, linear algebra, signal processing, and calculus.",
  openGraph: {
    title: "#KostasVisualizations",
    description: "Interactive visual explanations for projective geometry, optimization, linear algebra, signal processing, and calculus.",
    type: "website",
    images: [{ url: "/og.png", width: 1674, height: 909, alt: "#KostasVisualizations preview" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "#KostasVisualizations",
    description: "Interactive visual explanations for projective geometry, optimization, linear algebra, signal processing, and calculus.",
    images: ["/og.png"],
  },
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" data-theme="dark" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
