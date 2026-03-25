from embedder import embed_User_query
from vectorstore import search_in_pinecone
from llm import query_llm_with_context

def process_user_query(query: str):

    #Embed the user 's query to create a vector representation
    query_vector = embed_User_query(query)
    #Search the vector DB to find top matching chunks related to the user 's question
    matched_chunks = search_in_pinecone(query_vector)
    # Send the user query and the search results (query + context) to the LLM for generating response
    context = "\n\n".join(matched_chunks)
    answer = query_llm_with_context(query, context)
    return answer

if __name__ == "__main__":
    user_query = "Tell me about gifts and entertainment"
    print(process_user_query(user_query))