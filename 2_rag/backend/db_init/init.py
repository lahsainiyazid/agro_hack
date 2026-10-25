import sys
import asyncio 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from vectorstore import collection
from parsers import upload_documents 
DIR=Path("./documents")
files=list(DIR.glob("*.pdf"))
asyncio.run(upload_documents(files))
    
