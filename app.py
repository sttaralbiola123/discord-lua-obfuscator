from flask import Flask, render_template, request, jsonify
import os
from obfuscator import LuaObfuscator

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024

obfuscator = LuaObfuscator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/obfuscate', methods=['POST'])
def obfuscate_api():
    try:
        data = request.json
        code = data.get('code', '')
        level = data.get('level', 'medium')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        if level not in ['light', 'medium', 'heavy']:
            return jsonify({'error': 'Invalid level'}), 400
        
        if len(code) > 50000:
            return jsonify({'error': 'Code too long (max 50KB)'}), 400
        
        obfuscated = obfuscator.obfuscate(code, level)
        
        original_size = len(code.encode('utf-8'))
        obfuscated_size = len(obfuscated.encode('utf-8'))
        compression = ((original_size - obfuscated_size) / original_size * 100) if original_size > 0 else 0
        
        return jsonify({
            'success': True,
            'obfuscated': obfuscated,
            'stats': {
                'original_size': original_size,
                'obfuscated_size': obfuscated_size,
                'compression': round(compression, 2),
                'level': level.upper()
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/obfuscate-file', methods=['POST'])
def obfuscate_file_api():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        level = request.form.get('level', 'medium')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith(('.lua', '.txt')):
            return jsonify({'error': 'Invalid file type'}), 400
        
        code = file.read().decode('utf-8')
        
        if len(code) > 50000:
            return jsonify({'error': 'Code too long (max 50KB)'}), 400
        
        obfuscated = obfuscator.obfuscate(code, level)
        
        original_size = len(code.encode('utf-8'))
        obfuscated_size = len(obfuscated.encode('utf-8'))
        compression = ((original_size - obfuscated_size) / original_size * 100) if original_size > 0 else 0
        
        return jsonify({
            'success': True,
            'obfuscated': obfuscated,
            'stats': {
                'original_size': original_size,
                'obfuscated_size': obfuscated_size,
                'compression': round(compression, 2),
                'level': level.upper()
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
