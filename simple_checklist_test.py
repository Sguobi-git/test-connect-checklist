# simple_checklist_test.py
from abacusai import ApiClient
import json

def test_checklist_data():
    """Simple test to pull checklist data from Google Sheet"""
    
    # Your API key
    api_key = "s2_440d8b6da4094a9badee296fd7e6500d"  # Replace with your actual key
    
    # Same project ID as your working orders
    project_id = "16b4367d2c"
    
    print("🚀 Testing Checklist Data Extraction")
    print("=" * 50)
    
    try:
        # Create client (same as orders)
        client = ApiClient(api_key)
        print("✅ API Client created successfully")
        
        # Create chat session (same as orders)
        session = client.create_chat_session(project_id)
        print(f"✅ Chat session created: {session.chat_session_id}")
        
        # Test 1: Get all checklist data
        print("\n📋 Test 1: Getting all checklist data...")
        query1 = """Show me the first 10 rows from the checklist sheet. 
        Format as a simple table with columns: Booth #, Section, Exhibitor Name, Quantity, Item Name, Special Instructions, Status, Date, Hour"""
        
        response1 = client.get_chat_response(session.chat_session_id, query1)
        print("✅ Response received:")
        print("-" * 30)
        print(response1.content)
        print("-" * 30)
        
        # Test 2: Get specific booth data
        print("\n📋 Test 2: Getting booth 100 checklist data...")
        query2 = """Show me all checklist items for booth number 100 from the checklist sheet. 
        Format as a simple table with columns: Booth #, Section, Exhibitor Name, Quantity, Item Name, Special Instructions, Status, Date, Hour"""
        
        response2 = client.get_chat_response(session.chat_session_id, query2)
        print("✅ Response received:")
        print("-" * 30)
        print(response2.content)
        print("-" * 30)
        
        # Test 3: Try JSON format
        print("\n📋 Test 3: Getting data in JSON format...")
        query3 = """Show me checklist items for booth 100 from the checklist sheet in JSON format with these fields:
        {"Booth #": "", "Section": "", "Exhibitor Name": "", "Quantity": "", "Item Name": "", "Special Instructions": "", "Status": "", "Date": "", "Hour": ""}"""
        
        response3 = client.get_chat_response(session.chat_session_id, query3)
        print("✅ Response received:")
        print("-" * 30)
        print(response3.content)
        print("-" * 30)
        
        # Test 4: List available sheets
        print("\n📋 Test 4: Checking what sheets are available...")
        query4 = "What sheets or tables are available in this dataset? List all sheet names."
        
        response4 = client.get_chat_response(session.chat_session_id, query4)
        print("✅ Response received:")
        print("-" * 30)
        print(response4.content)
        print("-" * 30)
        
        print("\n🎉 All tests completed successfully!")
        print("💡 If you see checklist data above, the connection is working!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔍 Troubleshooting:")
        print("1. Check your API key")
        print("2. Make sure you have access to the checklist sheet")
        print("3. Verify the project ID is correct")

if __name__ == "__main__":
    test_checklist_data()
