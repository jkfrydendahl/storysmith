// Storysmith History Manager
// Manages localStorage for saving and retrieving generation history

const HistoryManager = {
  STORAGE_KEY: 'storysmith_history',
  MAX_ITEMS: 100, // Prevent unlimited growth

  // Save a generation to history
  save(type, parameters, content) {
    const history = this.getAll();
    const item = {
      id: Date.now(),
      type: type,
      parameters: parameters,
      content: content,
      timestamp: new Date().toISOString()
    };
    
    history.unshift(item); // Add to beginning
    
    // Keep only MAX_ITEMS
    if (history.length > this.MAX_ITEMS) {
      history.splice(this.MAX_ITEMS);
    }
    
    try {
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(history));
      return true;
    } catch (e) {
      console.error('Failed to save to history:', e);
      return false;
    }
  },

  // Get all history items
  getAll() {
    try {
      const data = localStorage.getItem(this.STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error('Failed to load history:', e);
      return [];
    }
  },

  // Get history items by type
  getByType(type) {
    return this.getAll().filter(item => item.type === type);
  },

  // Search history by content
  search(query) {
    const lowerQuery = query.toLowerCase();
    return this.getAll().filter(item => 
      item.content.toLowerCase().includes(lowerQuery) ||
      Object.values(item.parameters).some(val => 
        String(val).toLowerCase().includes(lowerQuery)
      )
    );
  },

  // Delete a specific item
  delete(id) {
    const history = this.getAll().filter(item => item.id !== id);
    try {
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(history));
      return true;
    } catch (e) {
      console.error('Failed to delete item:', e);
      return false;
    }
  },

  // Clear all history
  clearAll() {
    try {
      localStorage.removeItem(this.STORAGE_KEY);
      return true;
    } catch (e) {
      console.error('Failed to clear history:', e);
      return false;
    }
  },

  // Get count of items
  count() {
    return this.getAll().length;
  },

  // Get type display name
  getTypeDisplayName(type) {
    const names = {
      'character': '👤 Character',
      'location': '🗺️ Location',
      'item': '⚔️ Item',
      'treasure': '🏆 Treasure',
      'adventure': '🗡️ Adventure',
      'event': '🎭 Event',
      'organization': '🏛️ Organization',
      'region': '🗺️ Region',
      'weather': '🌤️ Weather',
      'creature': '🐉 Creature',
      'spell': '✨ Spell',
      'deity': '⚡ Deity'
    };
    return typeMap[type] || type;
  },

  // Format timestamp for display
  formatTimestamp(isoString) {
    const date = new Date(isoString);
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins} minute${diffMins > 1 ? 's' : ''} ago`;
    if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
    if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
    
    return date.toLocaleDateString();
  }
};
