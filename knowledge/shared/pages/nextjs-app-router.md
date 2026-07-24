---
title: "Next.js App Router — Overview & Best Practices"
tags: [nextjs, react, app-router, ssr, frontend]
keywords: [next.js, app router, server component, rsc, layouts, routing]
category: TechStack
last_updated: 2026-07-24
source: "https://nextjs.org/docs/app"
confidence: high
---

# Next.js App Router

> **ĐÂY LÀ FILE MẪU — xóa hoặc replace bằng nội dung thực khi ingest.**

## Overview
App Router (Next.js 13+) dùng React Server Components (RSC) làm default. Mọi component trong `app/` là Server Component trừ khi có `"use client"`.

## Key Concepts
- **Server Components**: render server-side, không có JS trên client, dùng cho data fetching
- **Client Components**: có `"use client"`, dùng cho interactivity, hooks, browser APIs
- **Layouts**: shared UI giữa routes, persist state, không re-render khi navigate
- **Route Handlers**: `app/api/route.ts` thay thế `pages/api/`

## Best Practices
- Data fetching trong Server Components — không dùng `useEffect` để fetch
- Colocate components với routes
- Dùng `loading.tsx` + `error.tsx` để handle states tự động

## Gotchas
- ⚠️ `useState`, `useEffect`, event handlers → phải có `"use client"`
- ⚠️ `cookies()`, `headers()` không dùng được trong Client Components
- ⚠️ Caching default khác với Pages Router — cần hiểu `revalidate`
