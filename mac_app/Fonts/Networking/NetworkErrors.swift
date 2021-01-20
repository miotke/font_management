//
//  NetworkErrors.swift
//  Fonts
//
//  Created by Miotke, Andrew on 1/20/21.
//

import Foundation

enum NetworkErrors: String, Error {
    case invalidFontFamily = "Invalid font family passed to URL"
    case unableToCompleteRequest = "Unable to complete request, check network connection"
    case invalidResponse = "Invalid response from URL. Response code did not return 200"
    case invalidData = "Data from API was invalid, check request"
}
