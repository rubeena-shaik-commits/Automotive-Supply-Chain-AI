# Automotive Supply Chain AI – Demand Forecasting & Inventory Optimization

## Project Overview
An AI-powered supply chain solution designed for automotive and manufacturing operations. It combines Machine Learning, inventory optimization, Retrieval-Augmented Generation (RAG), and Agentic AI to support better supply chain decisions.

## Business Problem
Manufacturing organizations need to predict component demand, maintain appropriate inventory levels, identify supplier performance issues, and reduce stockout risks.

## Project Objectives
- Forecast future component demand using Machine Learning.
- Calculate inventory position, safety stock, and reorder points.
- Recommend replenishment quantities.
- Analyze supplier performance.
- Retrieve relevant supplier information using RAG.
- Use an AI agent to coordinate analytical tools and explain results.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Random Forest Regression
- Sentence Transformers
- FAISS
- Microsoft Foundry
- GPT-5-mini
- Retrieval-Augmented Generation (RAG)
- Agentic AI
- Google Colab

## Project Architecture
1. Input datasets are loaded and processed.
2. A Random Forest model forecasts component demand.
3. Inventory optimization calculates reorder recommendations.
4. Supplier performance metrics are analyzed.
5. RAG retrieves relevant information from supplier documents.
6. An AI agent coordinates tools and generates explanations.

## Machine Learning
A Random Forest Regression model is used for demand forecasting with historical demand, lag features, rolling averages, and calendar features.

## Inventory Optimization
The solution calculates:
- Inventory Position
- Lead-Time Demand
- Safety Stock
- Reorder Point
- Recommended Order Quantity

## RAG
Supplier quality and logistics manuals are processed into text chunks, embedded, and indexed using FAISS for semantic retrieval.

## Agentic AI
An AI agent uses Python tools for demand forecasting, inventory analysis, supplier performance, document retrieval, and overall supply chain analysis.

## Dataset
This project uses synthetic manufacturing supply chain data for demonstration and learning purposes. It does not represent actual company or supplier data.

## Project Limitations
- Synthetic datasets are used.
- Supplier performance observations are limited.
- Recommendations require validation against real operational data.
- The agent provides recommendations only; it does not place purchase orders or contact suppliers.

## Future Enhancements
- Integrate real-time ERP and inventory data.
- Improve forecasting with additional external variables.
- Add supplier risk prediction.
- Build a web-based dashboard.
- Extend agent workflows with approval controls.

## Author
Python | Machine Learning | Generative AI | RAG | Agentic AI
