from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle


class EmbeddingService:
    def __init__(self, model_path="all-mpnet-base-v2", dim=768, index_path="data/index.faiss"):
        """
        Initialize the embedding service.
        - model_path: path or name of the SentenceTransformer model.
        - dim: dimension of the embeddings (768 for all-mpnet-base-v2).
        - index_path: where the FAISS index will be stored.
        """
        self.model = SentenceTransformer(model_path)   # Load the embedding model
        self.index_path = index_path                   # Path to FAISS index file
        self.meta_path = "data/meta.pkl"               # Path to store document metadata
        self.index = faiss.IndexFlatL2(dim)            # FAISS index (L2 distance)
        self.metadata = []                             # List of documents associated with embeddings

        os.makedirs("data", exist_ok=True)             # Ensure "data" directory exists
        self._load()                                   # Load previous index + metadata if available

    def _load(self):
        """
        Load FAISS index and metadata if they already exist on disk.
        """
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)   # Reload FAISS index
        if os.path.exists(self.meta_path):
            with open(self.meta_path, "rb") as f:
                self.metadata = pickle.load(f)               # Reload metadata

    def _save(self):
        """
        Save FAISS index and metadata to disk for persistence.
        """
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def add_documents(self, docs: list[dict]):
        """
        Add new documents into the system.
        Each document must be a dict containing at least a "content" field.
        - Encodes the text into embeddings.
        - Stores embeddings in FAISS index.
        - Persists original documents in metadata.
        - Saves everything to disk.
        Returns: number of documents added.
        """
        texts = [doc["content"] for doc in docs]                          # Extract raw text
        embeddings = self.model.encode(texts, convert_to_numpy=True)      # Generate embeddings
        self.index.add(embeddings)                                        # Add to FAISS
        self.metadata.extend(docs)                                        # Save metadata
        self._save()                                                      # Persist
        return len(docs)

    def search(self, query: str, k=5):
        """
        Perform semantic search for a given query.
        - Encodes the query into an embedding.
        - Searches for the top-k closest embeddings in FAISS.
        Returns: a list of dicts containing the matching document and its score.
        """
        query_emb = self.model.encode([query], convert_to_numpy=True)     # Encode query
        D, I = self.index.search(query_emb, k)                            # Search top-k results
        # D: Distancias (que tan diferentes son)
        # I: Indices (posiciones) dentro del indice FAISS de los vectores que coincidieron
        return [
            {"doc": self.metadata[idx], "score": float(D[0][pos])}
            for pos, idx in enumerate(I[0])
        ]


