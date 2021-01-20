//
//  NetworkManager.swift
//  Fonts
//
//  Created by Miotke, Andrew on 1/20/21.
//

import UIKit

class NetworkManager {
    static let shared = NetworkManager()
    
    // Change this to the actual URL when on a live server
    private let baseURL = "http://127.0.0.1:8000/"
    
    private init() {}
    
    func getFontFamilies(for fontFamily: String, page: Int, completed: @escaping(Result<[Font], NetworkErrors>) -> Void) {
        let endpoint = baseURL + "\(fontFamily)/"
        
        guard let url = URL(string: endpoint) else {
            completed(.failure(.invalidFontFamily))
            return
        }
        
        let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
            if let _ = error {
                completed(.failure(.unableToCompleteRequest))
                return
            }
            
            guard let response = response as? HTTPURLResponse, response.statusCode == 200 else {
                completed(.failure(.invalidResponse))
                return
            }
            
            guard let data = data else {
                completed(.failure(.invalidData))
                return
            }
            
            do {
                let decoder = JSONDecoder()
                decoder.keyDecodingStrategy = .convertFromSnakeCase
                let fontFamily = try decoder.decode([Font].self, from: data)
                completed(.success(fontFamily))
            } catch {
                completed(.failure(.invalidData))
            }
        }
        
        task.resume()
    }
}
